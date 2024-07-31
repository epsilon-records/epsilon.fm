import { OPENAI_API_KEY } from '$env/static/private';
import type { Config } from '@sveltejs/adapter-vercel';
import { OpenAIStream, StreamingTextResponse } from 'ai';
import type { RequestHandler } from './$types';
import { Configuration, OpenAIApi } from 'openai-edge';
import { kv } from '$lib/kv';
import { nanoid } from '$lib/utils';
import { currentUserId } from '$lib/stores/brain';

export const config: Config = {
	runtime: 'edge'
};

export const POST = (async ({ request }) => {
	try {
		const json = await request.json();
		const { messages } = json;

		const config = new Configuration({
			apiKey: OPENAI_API_KEY
		});

		// Create an instance of the OpenAI API client
		const openai = new OpenAIApi(config);

		// Ask OpenAI for a streaming chat completion given the prompt
		const response = await openai.createChatCompletion({
			model: 'gpt-3.5-turbo',
			messages,
			temperature: 0.7,
			stream: true
		});

		// Convert the response into a friendly text-stream
		const stream = OpenAIStream(response, {
			async onCompletion(completion) {
				const title = messages[0].content.substring(0, 100);
				if (currentUserId) {
					const id = json.id ?? nanoid();
					const createdAt = Date.now();
					const path = `/chat/${id}`;
					const payload = {
						id,
						title,
						currentUserId,
						createdAt,
						path,
						messages: [
							...messages,
							{
								content: completion,
								role: 'assistant'
							}
						]
					};
					await kv.hmset(`chat:${id}`, payload);
					await kv.zadd(`user:chat:${currentUserId}`, {
						score: createdAt,
						member: `chat:${id}`
					});
				}
			}
		});

		// Respond with the stream
		return new StreamingTextResponse(stream);
	} catch (error) {
		console.error('Error in chat API:', error);
		return new Response(
			JSON.stringify({ error: 'An error occurred while processing your request' }),
			{
				status: 500,
				headers: {
					'Content-Type': 'application/json'
				}
			}
		);
	}
}) satisfies RequestHandler;

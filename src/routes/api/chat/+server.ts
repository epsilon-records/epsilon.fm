import { OPENAI_API_KEY } from '$env/static/private';
import type { RequestHandler } from './$types';
import { kv } from '$lib/kv';
import { nanoid } from '$lib/utils';
import { currentUserId } from '$lib/stores/brain';
import { createOpenAI } from '@ai-sdk/openai';
import { streamText } from 'ai';

const openai = createOpenAI({
	apiKey: OPENAI_API_KEY ?? ''
});

export const POST = (async ({ request }) => {
	const json = await request.json();
	const { messages } = json;
	const result = await streamText({
		model: openai('gpt-3.5-turbo'),
		messages
	});
	const title = messages[0].content.substring(0, 100);
	if (currentUserId) {
		const id = json.id ?? nanoid();
		const createdAt = Date.now();
		const path = `/brain/chat/${id}`;
		const payload = {
			id,
			title,
			currentUserId,
			createdAt,
			path,
			messages: [
				...messages,
				{
					content: result,
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
	return result.toDataStreamResponse();
}) satisfies RequestHandler;

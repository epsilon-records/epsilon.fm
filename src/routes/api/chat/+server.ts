import { PERPLEXITY_API_KEY } from '$env/static/private';
import { createOpenAI } from '@ai-sdk/openai';
import { generateText } from 'ai';
import type { RequestHandler } from './$types';

const perplexity = createOpenAI({
	apiKey: PERPLEXITY_API_KEY,
	baseURL: 'https://api.perplexity.ai',
	compatibility: 'compatible'
});

export const POST = (async ({ request }) => {
	try {
		const { messages } = await request.json();
		const response = await generateText({
			model: perplexity('llama-3-sonar-large-32k-online'),
			messages: messages,
			temperature: 0.7
		});
		return new Response(JSON.stringify(response), {
			headers: {
				'Content-Type': 'application/json'
			}
		});
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

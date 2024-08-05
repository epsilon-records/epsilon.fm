import { json, error } from '@sveltejs/kit';
import type { RequestHandler } from './$types';

export const GET = (async ({ request }) => {
	const authHeader = request.headers.get('authorization');
	if (authHeader !== `Bearer ${process.env.CRON_SECRET}`) {
		throw error(401, 'Unauthorized');
	}
	console.log('Hello, world!');
	return json({ success: true });
}) satisfies RequestHandler;

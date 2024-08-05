import { json, error } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import { client, ArtistService } from '$lib/api/soundcharts/client/services.gen';
import { SOUNDCHARTS_API_URL, SOUNDCHARTS_API_KEY, SOUNDCHARTS_APP_ID } from '$env/static/private';

export const GET = (async ({ request }) => {
	const authHeader = request.headers.get('authorization');
	if (authHeader !== `Bearer ${process.env.CRON_SECRET}`) {
		throw error(401, 'Unauthorized');
	}
	console.log('Hello, world!');
	client.setConfig({
		baseUrl: SOUNDCHARTS_API_URL
	});
	client.interceptors.request.use((request) => {
		request.headers.set('x-api-key', SOUNDCHARTS_API_KEY);
		request.headers.set('x-app-id', SOUNDCHARTS_APP_ID);
		return request;
	});
	const response = await ArtistService.getApiV2ArtistByUuidAlbums({
		path: { uuid: '8fab7c54-0e0f-43a5-bf62-def4792d345a' }
	});
	console.log(response);
	if (response.data && response.data.items) {
		for (const album of response.data.items) {
			console.log(album);
		}
	}
	return json({ success: true });
}) satisfies RequestHandler;

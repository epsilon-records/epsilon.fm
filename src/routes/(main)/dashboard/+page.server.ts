import type { PageServerLoad } from './$types';
import { Musicfetch } from '$lib/consumer/musicfetch';
import { MUSIC_FETCH_API_KEY } from '$env/static/private';
import type { MusicfetchTrack } from '$lib/consumer/musicfetch';

export const load = (async () => {
	const musicfetch = new Musicfetch(MUSIC_FETCH_API_KEY);
	const trackUrl = 'https://open.spotify.com/track/0mrka7jzpLiieKpZmkrDr4?si=38a51b2f972246eb';
	const services = ['appleMusic', 'deezer', 'tidal'];

	let trackInfo: MusicfetchTrack | null = null;
	let error: string | null = null;

	try {
		trackInfo = await musicfetch.lookupTrack(trackUrl, services, 'US');
	} catch (err) {
		error = err instanceof Error ? err.message : String(err);
	}

	return { trackInfo, error };
}) satisfies PageServerLoad;

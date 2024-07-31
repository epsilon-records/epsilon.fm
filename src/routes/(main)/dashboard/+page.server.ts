import type { PageServerLoad } from './$types';
import { Musicfetch } from '$lib/consumer/musicfetch';
import { MUSICFETCH_API_KEY } from '$env/static/private';
import type { MusicfetchArtist } from '$lib/consumer/musicfetch';

export const load = (async () => {
	const musicfetch = new Musicfetch(MUSICFETCH_API_KEY);
	const trackUrl = 'https://open.spotify.com/track/0mrka7jzpLiieKpZmkrDr4';
	const services = ['appleMusic', 'deezer', 'tidal'];
	let artistInfo: MusicfetchArtist | null = null;
	let error: string | null = null;
	try {
		artistInfo = await musicfetch.lookupArtist(trackUrl, services, 'US');
	} catch (err) {
		error = err instanceof Error ? err.message : String(err);
	}
	return { artistInfo, error };
}) satisfies PageServerLoad;

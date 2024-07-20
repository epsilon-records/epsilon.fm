import { artistSchema } from '../routes/(main)/profile/schema';
import { API_URL, API_VERSION } from '$env/static/private';
import { z } from 'zod';

export const api = (customFetch = fetch) => ({
	getArtists: async (): Promise<z.infer<typeof artistSchema>[]> => {
		try {
			const response = await customFetch(`${API_URL}/${API_VERSION}/artist`);
			const data = await response.json();
			const parsedData = artistSchema.array().parse(data);
			return parsedData;
		} catch (error) {
			console.error('Error fetching artists:', error);
			throw new Error('Failed to fetch artists');
		}
	},
	getArtist: async (slug: string): Promise<z.infer<typeof artistSchema>> => {
		try {
			const response = await customFetch(`${API_URL}/${API_VERSION}/artist/${slug}`);
			const data = await response.json();
			const parsedData = artistSchema.parse(data);
			return parsedData;
		} catch (error) {
			console.error(`Error fetching artist with slug ${slug}:`, error);
			throw new Error(`Failed to fetch artist with slug ${slug}`);
		}
	}
});

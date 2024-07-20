import { artistSchema } from '../routes/(main)/profile/schema';
import { z } from 'zod';

class ArtistFetchError extends Error {
	constructor(message: string) {
		super(message);
		this.name = 'ArtistFetchError';
	}
}

export const api = (customFetch = fetch) => ({
	getArtists: async (): Promise<z.infer<typeof artistSchema>[]> => {
		try {
			const response = await customFetch('https://jsonplaceholder.typicode.com/posts');
			const data = await response.json();
			const parsedData = artistSchema.array().parse(data);
			return parsedData;
		} catch (error) {
			console.error('Error fetching artists:', error);
			throw new ArtistFetchError('Failed to fetch artists');
		}
	},
	getArtistById: async (id: number): Promise<z.infer<typeof artistSchema>> => {
		try {
			const response = await customFetch(`https://jsonplaceholder.typicode.com/posts/${id}`);
			const data = await response.json();
			const parsedData = artistSchema.parse(data);
			return parsedData;
		} catch (error) {
			console.error(`Error fetching artist with id ${id}:`, error);
			throw new ArtistFetchError(`Failed to fetch artist with id ${id}`);
		}
	}
});

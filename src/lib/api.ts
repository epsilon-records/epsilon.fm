import { type ArtistSchema } from '../routes/(main)/profile/schema';

export const api = (customFetch = fetch) => ({
	getArtists: async () => {
		const response = await customFetch('https://jsonplaceholder.typicode.com/posts');
		const data = (await response.json()) as ArtistSchema[];
		return data;
	},
	getArtistById: async (id: number): Promise<ArtistSchema> => {
		const response = await customFetch(`https://jsonplaceholder.typicode.com/posts/${id}`);
		const data = (await response.json()) as ArtistSchema;
		return data;
	}
});

import { artistSchema } from '../routes/(main)/profile/schema';
import { z } from 'zod';

export const api = (customFetch = fetch) => ({
	getArtists: async (): Promise<z.infer<typeof artistSchema>[]> => {
		const response = await customFetch('https://jsonplaceholder.typicode.com/posts');
		const data = await response.json();
		return artistSchema.array().parse(data); // Using Zod schema to parse and validate
	},
	getArtistById: async (id: number): Promise<z.infer<typeof artistSchema>> => {
		const response = await customFetch(`https://jsonplaceholder.typicode.com/posts/${id}`);
		const data = await response.json();
		console.log(data);
		console.log(artistSchema.parse(data));
		return artistSchema.parse(data); // Using Zod schema to parse and validate
	}
});

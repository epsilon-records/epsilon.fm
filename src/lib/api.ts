import { artistSchema } from '../routes/(main)/profile/schema';
import { PUBLIC_API_URL, PUBLIC_API_VERSION } from '$env/static/public';
import { z, ZodError } from 'zod';

class APIError extends Error {
	constructor(
		message: string,
		public status?: number
	) {
		super(message);
		this.name = 'APIError';
	}
}

const constructUrl = (path: string) => `${PUBLIC_API_URL}/${PUBLIC_API_VERSION}/${path}`;

/**
 * Represents an API object that provides methods for fetching artists and artist details.
 * @param customFetch - Optional custom fetch function to use for making HTTP requests.
 * @returns An API object with methods for fetching artists and artist details.
 */
export const api = (
	customFetch = fetch
): {
	getArtists: () => Promise<z.infer<typeof artistSchema>[]>;
	getArtist: (slug: string) => Promise<z.infer<typeof artistSchema>>;
} => ({
	/**
	 * Fetches an array of artists.
	 * @returns A promise that resolves to an array of artists.
	 * @throws {APIError} If the request fails or the response is not successful.
	 */
	getArtists: async (): Promise<z.infer<typeof artistSchema>[]> => {
		try {
			const response = await customFetch(constructUrl('artist'));
			if (!response.ok) {
				throw new APIError('Failed to fetch artists', response.status);
			}
			const data = await response.json();
			return artistSchema.array().parse(data);
		} catch (error) {
			console.error('Error fetching artists:', error);
			throw error instanceof APIError || error instanceof ZodError
				? error
				: new APIError('Failed to fetch artists');
		}
	},

	/**
	 * Fetches an artist by slug.
	 * @param slug - The slug of the artist to fetch.
	 * @returns A promise that resolves to the artist object.
	 * @throws {APIError} If the request fails or the response is not successful.
	 */
	getArtist: async (slug: string): Promise<z.infer<typeof artistSchema>> => {
		try {
			const response = await customFetch(constructUrl(`artist/${slug}`));
			if (!response.ok) {
				throw new APIError(`Failed to fetch artist with slug ${slug}`, response.status);
			}
			const data = await response.json();
			return artistSchema.parse(data);
		} catch (error) {
			console.error(`Error fetching artist with slug ${slug}:`, error);
			throw error instanceof APIError || error instanceof ZodError
				? error
				: new APIError(`Failed to fetch artist with slug ${slug}`);
		}
	}
});

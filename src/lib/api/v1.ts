import { artistSchema } from '$lib/schema';
import { PUBLIC_API_URL, PUBLIC_API_VERSION } from '$env/static/public';
import { z, ZodError } from 'zod';
import { logger } from '$lib/logger';

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
 * Generic function to fetch and parse data from the API
 * @param path - The API path to fetch from
 * @param schema - The Zod schema to parse the response with
 * @param customFetch - The fetch function to use
 * @returns Parsed data
 * @throws {APIError} If the request fails or the response is not successful
 */
async function fetchAndParse<T>(
	path: string,
	schema: z.ZodType<T>,
	customFetch: typeof fetch
): Promise<T> {
	try {
		const response = await customFetch(constructUrl(path));
		if (!response.ok) {
			throw new APIError(`Failed to fetch data from ${path}`, response.status);
		}
		const data = await response.json();
		return schema.parse(data);
	} catch (error) {
		logger.error(error);
		throw error instanceof APIError || error instanceof ZodError
			? error
			: new APIError(`Failed to fetch data from ${path}`);
	}
}

/**
 * Represents an API object that provides methods for fetching artists and artist details.
 * @param customFetch - Optional custom fetch function to use for making HTTP requests.
 * @returns An API object with methods for fetching artists and artist details.
 */
export const api = (
	customFetch: typeof fetch = fetch
): {
	getArtists: () => Promise<z.infer<typeof artistSchema>[]>;
	getArtist: (slug: string) => Promise<z.infer<typeof artistSchema>>;
} => ({
	/**
	 * Fetches an array of artists.
	 * @returns A promise that resolves to an array of artists.
	 */
	getArtists: () => fetchAndParse('artists', artistSchema.array(), customFetch),

	/**
	 * Fetches an artist by slug.
	 * @param slug - The slug of the artist to fetch.
	 * @returns A promise that resolves to the artist object.
	 */
	getArtist: (slug: string) => fetchAndParse(`artists/${slug}`, artistSchema, customFetch)
});

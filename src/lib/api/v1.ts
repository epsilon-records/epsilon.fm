import { artistSchema } from '$lib/schema';
import { env } from '$env/dynamic/public';
import { z, ZodError } from 'zod';
import logger from '$lib/logger';

class APIError extends Error {
	constructor(
		message: string,
		public status?: number
	) {
		super(message);
		this.name = 'APIError';
	}
}

const constructUrl = (path: string) => `${env.PUBLIC_API_URL}/${env.PUBLIC_API_VERSION}/${path}`;

/**
 * Generic function to fetch from the API
 * @param path - The API path to fetch from
 * @param schema - The Zod schema to parse the response with
 * @param customFetch - The fetch function to use
 * @returns Parsed data
 * @throws {APIError} If the request fails or the response is not successful
 */
async function fetchData<T>(
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
		console.log(data);
		return schema.parse(data);
	} catch (error) {
		logger.error(error);
		throw error instanceof APIError || error instanceof ZodError
			? error
			: new APIError(`Failed to fetch data from ${path}`);
	}
}

/**
 * Generic function to write data to the API
 * @param path - The API path to write to
 * @param method - The HTTP method to use (POST, PUT)
 * @param body - The body data to send
 * @param schema - The Zod schema to parse the response with
 * @param customFetch - The fetch function to use
 * @returns Parsed response data
 * @throws {APIError} If the request fails or the response is not successful
 */
async function writeData<T>(
	path: string,
	method: 'POST' | 'PUT',
	body: T,
	schema: z.ZodType<T>,
	customFetch: typeof fetch
): Promise<T> {
	try {
		const response = await customFetch(constructUrl(path), {
			method,
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(body)
		});
		if (!response.ok) {
			throw new APIError(`Failed to write data to ${path}`, response.status);
		}
		const data = await response.json();
		console.log(data);
		return schema.parse(data);
	} catch (error) {
		logger.error(error);
		throw error instanceof APIError || error instanceof ZodError
			? error
			: new APIError(`Failed to write data to ${path}`);
	}
}

/**
 * Represents an API object that provides methods for fetching and writing artist data.
 * @param customFetch - Optional custom fetch function to use for making HTTP requests.
 * @returns An API object with methods for fetching and writing artist data.
 */
export const api = (
	customFetch: typeof fetch = fetch
): {
	getArtists: () => Promise<z.infer<typeof artistSchema>[]>;
	getArtist: (slug: string) => Promise<z.infer<typeof artistSchema>>;
	writeArtist: (artist: z.infer<typeof artistSchema>) => Promise<z.infer<typeof artistSchema>>;
	updateArtist: (
		slug: string,
		artist: z.infer<typeof artistSchema>
	) => Promise<z.infer<typeof artistSchema>>;
} => ({
	/**
	 * Fetches an array of artists.
	 * @returns A promise that resolves to an array of artists.
	 */
	getArtists: () => fetchData('artists', artistSchema.array(), customFetch),

	/**
	 * Fetches an artist by slug.
	 * @param org_id - The organization ID of the artist to fetch.
	 * @returns A promise that resolves to the artist object.
	 */
	getArtist: (org_id: string) => fetchData(`artists/${org_id}`, artistSchema, customFetch),

	/**
	 * Writes (inserts or updates) a new artist.
	 * @param artist - The artist data to insert.
	 * @returns A promise that resolves to the inserted artist object.
	 */
	writeArtist: (artist) => writeData('artists', 'POST', artist, artistSchema, customFetch),

	/**
	 * Updates an existing artist.
	 * @param slug - The slug of the artist to update.
	 * @param artist - The artist data to update.
	 * @returns A promise that resolves to the updated artist object.
	 */
	updateArtist: (org_id: string, artist) =>
		writeData(`artists/${org_id}`, 'PUT', artist, artistSchema, customFetch)
});

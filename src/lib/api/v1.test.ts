import { describe, it, expect, vi } from 'vitest';
import { api } from '$lib/api/v1';
import { artistSchema } from '../schema';
import { z } from 'zod';

vi.mock('$env/static/public', () => ({
	PUBLIC_API_URL: 'http://mock-api.com',
	PUBLIC_API_VERSION: 'v1'
}));

const createMockFetch = (status: number, data: unknown) => {
	return vi.fn().mockResolvedValue({
		ok: status >= 200 && status < 300,
		status,
		json: async () => data
	});
};

const mockArtists: z.infer<typeof artistSchema>[] = [
	{
		id: '123e4567-e89b-12d3-a456-426614174000',
		orgId: 'org123',
		slug: 'artist-one',
		stageName: 'Artist One',
		email: 'artist.one@example.com',
		biography: 'Artist One is a talented musician with a unique sound.',
		spotifyArtistLink: 'https://open.spotify.com/artist/123',
		youtubeChannelLink: 'https://www.youtube.com/channel/123',
		instagramProfileLink: 'https://www.instagram.com/artistone',
		facebookProfileLink: 'https://www.facebook.com/artistone',
		xProfileLink: 'https://x.com/artistone',
		tiktokProfileLink: 'https://www.tiktok.com/@artistone',
		soundcloudProfileLink: 'https://soundcloud.com/artistone',
		songkickProfileLink: 'https://www.songkick.com/artists/123-artist-one',
		bandsintownProfileLink: 'https://www.bandsintown.com/a/123-artist-one'
	},
	{
		id: 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
		orgId: 'org456',
		slug: 'artist-two',
		stageName: 'Artist Two',
		email: 'artist.two@example.com',
		biography: 'Artist Two is a rising star in the electronic music scene.',
		spotifyArtistLink: 'https://open.spotify.com/artist/456',
		youtubeChannelLink: 'https://www.youtube.com/channel/456',
		instagramProfileLink: 'https://www.instagram.com/artisttwo',
		facebookProfileLink: 'https://www.facebook.com/artisttwo'
	}
];

describe('API Tests', () => {
	it('getArtists should return an array of artists', async () => {
		const mockFetch = createMockFetch(200, mockArtists);
		const apiInstance = api(mockFetch);

		const result = await apiInstance.getArtists();

		expect(result).toHaveLength(2);
		expect(result).toEqual(
			expect.arrayContaining([
				expect.objectContaining({ slug: 'artist-one' }),
				expect.objectContaining({ slug: 'artist-two' })
			])
		);
	});

	it('getArtists should throw an APIError on failed request', async () => {
		const mockFetch = createMockFetch(500, null);
		const apiInstance = api(mockFetch);

		await expect(apiInstance.getArtists()).rejects.toThrow('Failed to fetch data from artists');
	});

	it('getArtist should return a single artist', async () => {
		const mockArtist = mockArtists[0]; // Use the first mock artist

		const mockFetch = createMockFetch(200, mockArtist);
		const apiInstance = api(mockFetch);

		const result = await apiInstance.getArtist('artist-one');

		expect(result).toEqual(
			expect.objectContaining({
				slug: 'artist-one',
				stageName: 'Artist One'
			})
		);
	});

	it('getArtist should throw an APIError on failed request', async () => {
		const mockFetch = createMockFetch(404, null);
		const apiInstance = api(mockFetch);

		await expect(apiInstance.getArtist('nonexistent')).rejects.toThrow(
			'Failed to fetch data from artists/nonexistent'
		);
	});

	it('API should correctly parse valid data', async () => {
		const validArtist = mockArtists[0];
		const mockFetch = createMockFetch(200, validArtist);
		const apiInstance = api(mockFetch);

		const result = await apiInstance.getArtist('artist-one');
		expect(() => artistSchema.parse(result)).not.toThrow();
	});

	it('API should throw on invalid data', async () => {
		const invalidArtist = {
			id: 'not-a-number',
			orgId: 123,
			slug: 'invalid-artist',
			stageName: 'Invalid Artist',
			email: 'not-an-email'
		};

		const mockFetch = createMockFetch(200, invalidArtist);
		const apiInstance = api(mockFetch);

		await expect(apiInstance.getArtist('invalid-artist')).rejects.toThrow(z.ZodError);
	});
});

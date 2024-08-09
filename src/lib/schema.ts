import { z } from 'zod';

const artistSchema = z.object({
	id: z.string().uuid().optional(),
	created_at: z.string().datetime({ offset: true }).optional(),
	updated_at: z.string().datetime({ offset: true }).optional(),
	org_id: z.string().max(255),
	slug: z.string().max(255),
	stage_name: z.string().max(50),
	media_url: z.string().url().nullable().optional(),
	email: z.string().max(255),
	biography: z.string().max(1000),
	spotify_artist_link: z.string().max(255).optional(),
	youtube_channel_link: z.string().max(255).optional(),
	instagram_profile_link: z.string().max(255).optional(),
	facebook_profile_link: z.string().max(255).optional(),
	x_profile_link: z.string().max(255).optional(), // X refers to Twitter
	tiktok_profile_link: z.string().max(255).optional(),
	soundcloud_profile_link: z.string().max(255).optional(),
	songkick_profile_link: z.string().max(255).optional(),
	bandsintown_profile_link: z.string().max(255).optional(),
	apple_artist_link: z.string().max(255).optional(),
	beatport_artist_link: z.string().max(255).optional(),
	deezer_artist_link: z.string().max(255).optional(),
	tidal_artist_link: z.string().max(255).optional(),
	pandora_artist_link: z.string().max(255).optional(),
	shazam_artist_link: z.string().max(255).optional()
});

const genreSchema = z.object({
	id: z.string().uuid().optional(),
	name: z.string().max(50)
});

const releaseSchema = z.object({
	id: z.string().uuid().optional(),
	artistId: z.number(),
	title: z.string().max(100),
	releaseDate: z.string(), // Using string to represent date
	description: z.string().optional(),
	spotifyLink: z.string().max(255).optional(),
	youtubeLink: z.string().max(255).optional(),
	soundcloudLink: z.string().max(255).optional(),
	appleMusicLink: z.string().max(255).optional(),
	coverArt: z.string().max(255).optional(),
	label: z.string().max(100).optional(),
	releaseType: z.string().max(50).optional(), // Single, Album, EP, etc.
	format: z.string().max(50).optional(), // Digital, Vinyl, CD, etc.
	upcCode: z.string().max(20).optional() // Universal Product Code
});

const trackSchema = z.object({
	id: z.string().uuid().optional(),
	releaseId: z.number(),
	title: z.string().max(100),
	preview: z.number(),
	position: z.number(),
	genreId: z.number(),
	spotifyLink: z.string().max(255).optional(),
	youtubeLink: z.string().max(255).optional(),
	soundcloudLink: z.string().max(255).optional(),
	appleMusicLink: z.string().max(255).optional(),
	isrcCode: z.string().max(20).optional(), // International Standard Recording Code
	lyrics: z.string().optional(), // Lyrics of the track
	composers: z.string().optional(), // List of composers
	producers: z.string().optional(), // List of producers
	engineers: z.string().optional(), // List of engineers
	mixingEngineers: z.string().optional(), // List of mixing engineers
	masteringEngineers: z.string().optional(), // List of mastering engineers
	recordingLocation: z.string().max(255).optional(), // Studio or location of recording
	credits: z.string().optional() // Additional credits
});

const trackSubgenreSchema = z.object({
	trackId: z.string().uuid(),
	subgenreId: z.string().uuid()
});

export type ArtistSchema = typeof artistSchema;

export { artistSchema, genreSchema, releaseSchema, trackSchema, trackSubgenreSchema };

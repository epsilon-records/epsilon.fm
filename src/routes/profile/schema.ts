import { z } from 'zod';

const artistSchema = z.object({
	id: z.number().optional(),
	firstName: z.string().max(50),
	lastName: z.string().max(50),
	stageName: z.string().max(50).optional(),
	email: z.string().max(100),
	birthdate: z.string(), // Using string to represent date
	phone: z.string().max(15).optional(),
	address: z.string().optional(),
	biography: z.string().optional(),
	spotifyArtistLink: z.string().max(255).optional(),
	youtubeChannelLink: z.string().max(255).optional(),
	instagramProfileLink: z.string().max(255).optional(),
	facebookProfileLink: z.string().max(255).optional(),
	xProfileLink: z.string().max(255).optional(), // X refers to Twitter
	tiktokProfileLink: z.string().max(255).optional(),
	soundcloudProfileLink: z.string().max(255).optional(),
	songkickProfileLink: z.string().max(255).optional(),
	bandsintownProfileLink: z.string().max(255).optional(),
	referralSource: z.string().max(255).optional(), // Better column name for how_did_you_hear_about_us
	anrReferral: z.string().max(255).optional()
});

const genreSchema = z.object({
	id: z.number().optional(),
	name: z.string().max(50)
});

const releaseSchema = z.object({
	id: z.number().optional(),
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
	id: z.number().optional(),
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
	trackId: z.number(),
	subgenreId: z.number()
});

export type ArtistSchema = typeof artistSchema;

export { artistSchema, genreSchema, releaseSchema, trackSchema, trackSubgenreSchema };

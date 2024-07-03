import { boolean, timestamp, pgTable, text, primaryKey, integer } from 'drizzle-orm/pg-core';
import { drizzle } from 'drizzle-orm/postgres-js';
import type { AdapterAccountType } from '@auth/core/adapters';
import { sql } from '@vercel/postgres';

export const db = drizzle(sql);

export const users = pgTable('user', {
	id: text('id')
		.primaryKey()
		.$defaultFn(() => crypto.randomUUID()),
	name: text('name'),
	email: text('email').notNull(),
	emailVerified: timestamp('emailVerified', { mode: 'date' }),
	image: text('image')
});

export const accounts = pgTable(
	'account',
	{
		userId: text('userId')
			.notNull()
			.references(() => users.id, { onDelete: 'cascade' }),
		type: text('type').$type<AdapterAccountType>().notNull(),
		provider: text('provider').notNull(),
		providerAccountId: text('providerAccountId').notNull(),
		refresh_token: text('refresh_token'),
		access_token: text('access_token'),
		expires_at: integer('expires_at'),
		token_type: text('token_type'),
		scope: text('scope'),
		id_token: text('id_token'),
		session_state: text('session_state')
	},
	(account) => ({
		compoundKey: primaryKey({
			columns: [account.provider, account.providerAccountId]
		})
	})
);

export const sessions = pgTable('session', {
	sessionToken: text('sessionToken').primaryKey(),
	userId: text('userId')
		.notNull()
		.references(() => users.id, { onDelete: 'cascade' }),
	expires: timestamp('expires', { mode: 'date' }).notNull()
});

export const verificationTokens = pgTable(
	'verificationToken',
	{
		identifier: text('identifier').notNull(),
		token: text('token').notNull(),
		expires: timestamp('expires', { mode: 'date' }).notNull()
	},
	(verificationToken) => ({
		compositePk: primaryKey({
			columns: [verificationToken.identifier, verificationToken.token]
		})
	})
);

export const authenticators = pgTable(
	'authenticator',
	{
		credentialID: text('credentialID').notNull().unique(),
		userId: text('userId')
			.notNull()
			.references(() => users.id, { onDelete: 'cascade' }),
		providerAccountId: text('providerAccountId').notNull(),
		credentialPublicKey: text('credentialPublicKey').notNull(),
		counter: integer('counter').notNull(),
		credentialDeviceType: text('credentialDeviceType').notNull(),
		credentialBackedUp: boolean('credentialBackedUp').notNull(),
		transports: text('transports')
	},
	(authenticator) => ({
		compositePK: primaryKey({
			columns: [authenticator.userId, authenticator.credentialID]
		})
	})
);

export const artist = pgTable('artist', {
	id: serial('id').primaryKey(),
	firstName: varchar('first_name', { length: 50 }).notNull(),
	lastName: varchar('last_name', { length: 50 }).notNull(),
	stageName: varchar('stage_name', { length: 50 }),
	email: varchar('email', { length: 100 }).notNull(),
	birthdate: date('birthdate').notNull(),
	phone: varchar('phone', { length: 15 }),
	address: text('address'),
	biography: text('biography'),
	spotifyArtistLink: varchar('spotify_artist_link', { length: 255 }),
	youtubeChannelLink: varchar('youtube_channel_link', { length: 255 }),
	instagramProfileLink: varchar('instagram_profile_link', { length: 255 }),
	facebookProfileLink: varchar('facebook_profile_link', { length: 255 }),
	xProfileLink: varchar('x_profile_link', { length: 255 }), // X refers to Twitter
	tiktokProfileLink: varchar('tiktok_profile_link', { length: 255 }),
	soundcloudProfileLink: varchar('soundcloud_profile_link', { length: 255 }),
	songkickProfileLink: varchar('songkick_profile_link', { length: 255 }),
	bandsintownLink: varchar('bandsintown_link', { length: 255 }),
	referralSource: varchar('referral_source', { length: 255 }), // Better column name for how_did_you_hear_about_us
	anrReferral: varchar('anr_referral', { length: 255 })
});

export const genre = pgTable('genre', {
	id: serial('id').primaryKey(),
	name: varchar('name', { length: 50 }).notNull()
});

export const release = pgTable('release', {
	id: serial('id').primaryKey(),
	artistId: integer('artist_id')
		.references(() => artist.id)
		.notNull(),
	title: varchar('title', { length: 100 }).notNull(),
	releaseDate: date('release_date').notNull(),
	description: text('description'),
	spotifyLink: varchar('spotify_link', { length: 255 }),
	youtubeLink: varchar('youtube_link', { length: 255 }),
	soundcloudLink: varchar('soundcloud_link', { length: 255 }),
	appleMusicLink: varchar('apple_music_link', { length: 255 }),
	coverArt: varchar('cover_art', { length: 255 }),
	label: varchar('label', { length: 100 }),
	releaseType: varchar('release_type', { length: 50 }), // Single, Album, EP, etc.
	format: varchar('format', { length: 50 }), // Digital, Vinyl, CD, etc.
	upcCode: varchar('upc_code', { length: 20 }) // Universal Product Code
});

export const track = pgTable('track', {
	id: serial('id').primaryKey(),
	releaseId: integer('release_id')
		.references(() => release.id)
		.notNull(),
	title: varchar('title', { length: 100 }).notNull(),
	preview: decimal('duration').notNull(), // Start time of the track in seconds
	position: integer('position').notNull(), // Position of the track in the release
	genreId: integer('genre_id')
		.references(() => genre.id)
		.notNull(),
	spotifyLink: varchar('spotify_link', { length: 255 }),
	youtubeLink: varchar('youtube_link', { length: 255 }),
	soundcloudLink: varchar('soundcloud_link', { length: 255 }),
	appleMusicLink: varchar('apple_music_link', { length: 255 }),
	isrcCode: varchar('isrc_code', { length: 20 }), // International Standard Recording Code
	lyrics: text('lyrics'), // Lyrics of the track
	composers: text('composers'), // List of composers
	producers: text('producers'), // List of producers
	engineers: text('engineers'), // List of engineers
	mixingEngineers: text('mixing_engineers'), // List of mixing engineers
	masteringEngineers: text('mastering_engineers'), // List of mastering engineers
	recordingLocation: varchar('recording_location', { length: 255 }), // Studio or location of recording
	credits: text('credits') // Additional credits
});

export const trackSubgenre = pgTable(
	'track_subgenre',
	{
		trackId: integer('track_id')
			.references(() => track.id)
			.notNull(),
		subgenreId: integer('subgenre_id')
			.references(() => genre.id)
			.notNull()
	},
	(table) => {
		return {
			pk: primaryKey({ columns: [table.trackId, table.subgenreId] })
		};
	}
);

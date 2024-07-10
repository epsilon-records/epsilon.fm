import {
	pgTable,
	serial,
	text,
	primaryKey,
	integer,
	varchar,
	date,
	decimal
} from 'drizzle-orm/pg-core';

export const user = pgTable('user', {
	id: serial('id').primaryKey(),
	authId: varchar('auth_id', { length: 255 }).notNull(),
	birthdate: date('birthdate').notNull(),
	phone: varchar('phone', { length: 15 }),
	address: text('address'),
	referralSource: varchar('referral_source', { length: 255 }), // Better column name for how_did_you_hear_about_us
	anrReferral: varchar('anr_referral', { length: 255 })
});

export const artist = pgTable('artist', {
	id: serial('id').primaryKey(),
	orgId: varchar('org_id', { length: 255 }).unique().notNull(),
	stageName: varchar('stage_name', { length: 50 }),
	biography: text('biography'),
	spotifyArtistLink: varchar('spotify_artist_link', { length: 255 }),
	youtubeChannelLink: varchar('youtube_channel_link', { length: 255 }),
	instagramProfileLink: varchar('instagram_profile_link', { length: 255 }),
	facebookProfileLink: varchar('facebook_profile_link', { length: 255 }),
	xProfileLink: varchar('x_profile_link', { length: 255 }), // X refers to Twitter
	tiktokProfileLink: varchar('tiktok_profile_link', { length: 255 }),
	soundcloudProfileLink: varchar('soundcloud_profile_link', { length: 255 }),
	songkickProfileLink: varchar('songkick_profile_link', { length: 255 }),
	bandsintownProfileLink: varchar('bandsintown_profile_link', { length: 255 }),
	updatedAt: timestamp('updated_at').defaultNow().notNull()
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
	upcCode: varchar('upc_code', { length: 20 }), // Universal Product Code
	updatedAt: timestamp('updated_at').defaultNow().notNull()
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
	credits: text('credits'), // Additional credits
	updatedAt: timestamp('updated_at').defaultNow().notNull()
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

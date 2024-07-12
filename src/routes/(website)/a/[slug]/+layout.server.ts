import type { LayoutServerLoad } from './$types';
import { clerkClient } from '@clerk/clerk-sdk-node';
import { db } from '$lib/db';
import { artist } from '$lib/db/schema';
import { eq } from 'drizzle-orm';
import { redirect } from '@sveltejs/kit';

export const load = (async ({ params }) => {
	const response = await clerkClient.organizations.getOrganization({
		slug: params.slug
	});
	const data = await db
		.select()
		.from(artist)
		.where(eq(artist.orgId, response.id ?? null));
	if (data.length != 0) {
		return {
			stageName: response.name ?? null,
			imageUrl: response.imageUrl ?? null,
			slug: params.slug,
			email: response.email ?? null,
			biography: data[0].biography ?? null,
			youtubeChannelLink: data[0].youtubeChannelLink ?? null,
			instagramProfileLink: data[0].instagramProfileLink ?? null,
			facebookProfileLink: data[0].facebookProfileLink ?? null,
			tiktokProfileLink: data[0].tiktokProfileLink ?? null,
			soundcloudProfileLink: data[0].soundcloudProfileLink ?? null,
			songkickProfileLink: data[0].songkickProfileLink ?? null,
			bandsintownProfileLink: data[0].bandsintownProfileLink ?? null
		};
	} else {
		redirect(404, '/');
	}
}) satisfies LayoutServerLoad;

import { clerkClient } from '@clerk/clerk-sdk-node';
import { db } from '$lib/db';
import { artist } from '$lib/db/schema';
import { eq } from 'drizzle-orm';
import { redirect } from '@sveltejs/kit';

/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
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
}

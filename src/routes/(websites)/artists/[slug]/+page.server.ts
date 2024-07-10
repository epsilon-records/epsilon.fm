import { clerkClient } from '@clerk/clerk-sdk-node';
import { db } from '$lib/db';
import { redirect } from '@sveltejs/kit';

/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
	const response = await clerkClient.organizations.getOrganization({
		slug: params.slug
	});
	const organizationId = response.id ?? null;
	const stageName = response.name ?? null;
	const data = await db.select().from(artist).where(eq(artist.orgId, organizationId));
	if (data.length != 0) {
		return {
			stageName: stageName,
			instagramProfileLink: response.instagramProfileLink ?? null,
			facebookProfileLink: response.facebookProfileLink ?? null,
			tiktokProfileLink: response.tiktokProfileLink ?? null,
			soundcloudProfileLink: response.soundcloudProfileLink ?? null,
			songkickProfileLink: response.songkickProfileLink ?? null,
			bandsintownProfileLink: response.bandsintownProfileLink ?? null
		};
	} else {
		redirect(404, '/');
	}
}

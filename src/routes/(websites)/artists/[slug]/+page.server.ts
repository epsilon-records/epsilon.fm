import { clerkClient } from '@clerk/clerk-sdk-node';
import { db } from '$lib/db';
import { redirect } from '@sveltejs/kit';
import { eq } from 'drizzle-orm';

/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
	try {
		const { slug } = params;
		const response = await clerkClient.organizations.getOrganization({ slug });
		const { id: organizationId, name: stageName } = response;

		if (!organizationId) {
			throw new Error('Organization ID not found.');
		}

		const data = await db.select().from('artist').where(eq(artist.orgId, organizationId));

		if (!data.length) {
			redirect(404, '/');
		}

		const {
			instagramProfileLink = null,
			facebookProfileLink = null,
			tiktokProfileLink = null,
			soundcloudProfileLink = null,
			songkickProfileLink = null,
			bandsintownProfileIdk = null
		} = response;

		const profileLinks = {
			instagramProfileLink,
			facebookProfileLink,
			tiktokProfileLink,
			soundcloudProfileLink,
			songkickProfileLink,
			bandsintownProfileIdk
		};

		return { stageName, ...profileLinks };
	} catch (error) {
		console.error('Failed to load data:', error);
		redirect(500, '/error');
	}
}

import { clerkClient } from '@clerk/clerk-sdk-node';

/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
	const response = await clerkClient.organizations.getOrganization({
		slug: params.slug
	});
	const stageName = response.name ?? null;
	return {
		stageName: stageName
	};
}

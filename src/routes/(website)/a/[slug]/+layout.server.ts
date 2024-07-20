import type { LayoutServerLoad } from './$types';
import { clerkClient } from '@clerk/clerk-sdk-node';

export const load = (async ({ params }) => {
	const response = await clerkClient.organizations.getOrganization({
		slug: params.slug
	});
	return {
		orgId: response.id ?? null,
		stageName: response.name ?? null,
		imageUrl: response.imageUrl ?? null,
		slug: response.slug ?? null,
		email: 'hello@epsilonrecords.com' ?? null
	};
}) satisfies LayoutServerLoad;

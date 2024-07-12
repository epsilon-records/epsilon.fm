import type { PageServerLoad } from './$types.js';
import { clerkClient } from '@clerk/clerk-sdk-node';

export const load: PageServerLoad = async ({ locals }) => {
	const organizationId = locals.session.claims.org_id ?? null;
	const response = await clerkClient.organizations.getOrganization({ organizationId });
	console.log('TEST' + response);
	const slug = response.slug ?? null;
	return {
		slug: slug
	};
};

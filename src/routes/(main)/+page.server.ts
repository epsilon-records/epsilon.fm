import type { PageServerLoad } from './$types.js';
import { clerkClient } from '@clerk/clerk-sdk-node';

export  load: PageServerLoad = async ({ locals }) => {
	const organizationId = locals.session.claims.org_id ?? null;
	const response = await clerkClient.organizations.getOrganization({ organizationId });
	return {
		slug: response.slug ?? ''
	};
};

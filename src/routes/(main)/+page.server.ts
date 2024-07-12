import type { PageServerLoad } from './$types.js';
import { clerkClient } from '@clerk/clerk-sdk-node';

export const load: PageServerLoad = async ({ locals }) => {
	let slug = '';
	if (locals.session.claims) {
		const organizationId = locals.session.claims.org_id ?? null;
		const response = await clerkClient.organizations.getOrganization({ organizationId });
		slug = response.slug ?? '';
	}
	return {
		slug: slug
	};
};

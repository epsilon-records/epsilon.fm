import type { PageServerLoad } from './$types.js';
import { clerkClient } from '@clerk/clerk-sdk-node';

export const load: PageServerLoad = async ({ locals }) => {
	let slug = '';
	console.log('TEST');
	console.log('HI' + locals);
	if (locals.session !== undefined) {
		const organizationId = locals.session.claims.org_id ?? null;
		const response = await clerkClient.organizations.getOrganization({ organizationId });
		slug = response.slug ?? '';
	}
	return {
		slug: slug
	};
};

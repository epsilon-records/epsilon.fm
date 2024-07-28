// import type { PageServerLoad } from './$types.js';
// import { clerkClient } from '@clerk/clerk-sdk-node';

// export const load: PageServerLoad = async ({ locals }) => {
// 	let slug = '';

// 	// Use type assertion to access 'session'
// 	const session = (locals as { session?: { claims?: { org_id?: string } } }).session;

// 	if (session && session.claims && session.claims.org_id) {
// 		const organizationId = session.claims.org_id;
// 		const response = await clerkClient.organizations.getOrganization({ organizationId });
// 		slug = response.slug ?? '';
// 	}

// 	return {
// 		slug: slug
// 	};
// };

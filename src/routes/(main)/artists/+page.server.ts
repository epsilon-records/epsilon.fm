import type { PageServerLoad } from './$types.js';
import { clerkClient } from '@clerk/clerk-sdk-node';

export const load: PageServerLoad = async () => {
	const response = await clerkClient.organizations.getOrganizationList({
		limit: 10,
		offset: 0,
		includeMembersCount: true
	});
	return {
		artists: JSON.parse(JSON.stringify(response.data))
	};
};

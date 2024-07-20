import { api } from '$lib/api';
import { clerkClient } from '@clerk/clerk-sdk-node';
import type { PageLoad } from './$types';

export const load: PageLoad = async ({ params, parent, fetch }) => {
	const response = await clerkClient.organizations.getOrganization({
		slug: params.slug
	});
	const { queryClient } = await parent();
	await queryClient.prefetchQuery({
		queryKey: ['artists'],
		queryFn: () => api(fetch).getArtist(response.id)
	});
};

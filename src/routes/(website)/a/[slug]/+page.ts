import type { PageLoad } from './$types';
import { api } from '$lib/api';

export const load = (async ({ parent }) => {
	const { queryClient, orgId } = await parent();
	await queryClient.prefetchQuery({
		queryKey: ['artist'],
		queryFn: async () => api().getArtist(orgId)
	});
}) satisfies PageLoad;

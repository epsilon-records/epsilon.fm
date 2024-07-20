import type { PageLoad } from './$types';
import { api } from '$lib/api/v1';

export const load = (async ({ parent }) => {
	const { queryClient, orgId } = await parent();
	await queryClient.prefetchQuery({
		queryKey: ['artists', orgId],
		queryFn: async () => api().getArtist(orgId)
	});
}) satisfies PageLoad;

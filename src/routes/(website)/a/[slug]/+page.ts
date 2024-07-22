import type { PageLoad } from './$types';
import { api } from '$lib/api/v1';

export const load = (async ({ parent }) => {
	const { queryClient, org_id } = await parent();
	await queryClient.prefetchQuery({
		queryKey: ['artists', org_id],
		queryFn: async () => api().getArtist(org_id)
	});
}) satisfies PageLoad;

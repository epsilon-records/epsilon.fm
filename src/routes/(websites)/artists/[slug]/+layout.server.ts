import type { LayoutServerLoad } from './$types';

export const load = (async ({ params }) => {
	return { slug: params.slug };
}) satisfies LayoutServerLoad;

import type { PageServerLoad } from './$types.js';
import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { artistSchema } from '$lib/schema';
import { clerkClient } from '@clerk/clerk-sdk-node';
import { fail } from '@sveltejs/kit';
import _ from 'lodash';
import { ArtistsService } from '$lib/api/ms/client/services.gen';

export const load: PageServerLoad = async ({ locals }) => {
	let form = await superValidate(zod(artistSchema));
	const session = _.get(locals, 'session') as { claims?: { org_id?: string } } | undefined;
	const org_id = _.get(session, 'claims.org_id');
	if (org_id) {
		const response = await clerkClient.organizations.getOrganization({ organizationId: org_id });
		const stage_name = _.get(response, 'name', null);
		const slug = _.get(response, 'slug', null);
		if (!stage_name || !slug) {
			return fail(500, { message: 'Organization data is incomplete' });
		}
		try {
			const artistData = await ArtistsService.endpointV1ArtistsGetIdGet({ path: { id: org_id } });
			if (artistData.response.ok && artistData.data) {
				form = await superValidate(artistData.data, zod(artistSchema), { strict: true });
			}
			if (!form.valid) {
				return fail(400, { form });
			}
		} catch (error) {
			console.error('Error fetching artist data:', error);
			return fail(400, { form });
		}
		form.data.org_id = org_id;
		form.data.stage_name = stage_name;
		form.data.slug = slug;
	}
	return {
		form: form
	};
};

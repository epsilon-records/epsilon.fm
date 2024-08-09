// import type { PageServerLoad, Actions } from './$types.js';
// import { message, superValidate } from 'sveltekit-superforms';
// import { zod } from 'sveltekit-superforms/adapters';
// import { artistSchema } from '$lib/schema';
// import { clerkClient } from '@clerk/clerk-sdk-node';
// import { fail } from '@sveltejs/kit';
// // import { ArtistsService } from '$lib/api/ms/client/services.gen';
// import _ from 'lodash';

// export const load: PageServerLoad = async ({ locals }) => {
// 	let form = await superValidate(zod(artistSchema));
// 	// Use type assertion to access 'session'
// 	const session = _.get(locals, 'session') as { claims?: { org_id?: string } } | undefined;
// 	const org_id = _.get(session, 'claims.org_id');
// 	if (org_id) {
// 		const response = await clerkClient.organizations.getOrganization({ organizationId: org_id });
// 		const stage_name = _.get(response, 'name', null);
// 		const slug = _.get(response, 'slug', null);
// 		if (!stage_name || !slug) {
// 			return fail(500, { message: 'Organization data is incomplete' });
// 		}
// 		try {
// 			const artistData = await api().getArtist(org_id); // Fetch data using the API
// 			if (artistData) {
// 				const formattedData = _.mapValues(artistData, (value) =>
// 					value === null ? undefined : value
// 				);
// 				form = await superValidate(formattedData, zod(artistSchema), { strict: true });
// 				if (!form.valid) {
// 					return fail(400, { form });
// 				}
// 			}
// 		} catch (error) {
// 			console.error('Error fetching artist data:', error);
// 			return fail(400, { form });
// 		}
// 		form.data.org_id = org_id;
// 		form.data.stage_name = stage_name;
// 		form.data.slug = slug;
// 	}
// 	return {
// 		form: form
// 	};
// };

// export const actions: Actions = {
// 	default: async ({ request }) => {
// 		const form = await superValidate(request, zod(artistSchema), { strict: true });
// 		if (!form.valid) {
// 			return fail(400, {
// 				form
// 			});
// 		}
// 		try {
// 			const updatedData = {
// 				...form.data,
// 				id: form.data.id?.toString()
// 			};

// 			// Check if the artist exists to decide whether to update or insert
// 			const existingArtist = await api().getArtist(form.data.org_id);
// 			if (existingArtist) {
// 				await api().updateArtist(form.data.org_id, updatedData); // Update existing artist
// 			} else {
// 				await api().writeArtist(updatedData); // Insert new artist
// 			}
// 		} catch (error) {
// 			console.error('Error writing or updating artist data:', error);
// 			return fail(500, {
// 				form,
// 				message: 'Error writing or updating artist data'
// 			});
// 		}
// 		return message(form, 'success');
// 	}
// };

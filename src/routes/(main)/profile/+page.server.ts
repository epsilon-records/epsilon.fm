import type { PageServerLoad, Actions } from './$types.js';
import { message, superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { artistSchema } from '$lib/schema.js';
import { clerkClient } from '@clerk/clerk-sdk-node';
import { fail } from '@sveltejs/kit';
import { api } from '$lib/api/v1';

export const load: PageServerLoad = async ({ locals }) => {
	// Use type assertion to access 'session'
	const session = (locals as { session?: { claims?: { org_id?: string } } }).session;
	let form = await superValidate(zod(artistSchema));
	if (session && session.claims && session.claims.org_id) {
		const org_id = session.claims.org_id ?? null;
		const response = await clerkClient.organizations.getOrganization({ organizationId: org_id });
		const stage_name = response.name ?? null;
		const slug = response.slug ?? null;
		if (!org_id || !stage_name || !slug) {
			return fail(500, { message: 'Organization data is incomplete' });
		}

		try {
			const data = await api().getArtists(); // Fetch data using the API
			if (data.length !== 0) {
				const artistData = data.find((artist) => artist.org_id === org_id);
				if (artistData) {
					// Convert null values to undefined
					const formattedData = Object.fromEntries(
						Object.entries(artistData).map(([key, value]) => [
							key,
							value === null ? undefined : value
						])
					);
					form = await superValidate(formattedData, zod(artistSchema), { strict: true });
				}
			}
		} catch (error) {
			console.error('Error fetching artist data:', error);
			return fail(500, { message: 'Error fetching artist data' });
		}

		form.data.org_id = org_id;
		form.data.stage_name = stage_name;
		form.data.slug = slug;
	}
	return {
		form: form
	};
};

export const actions: Actions = {
	default: async ({ request }) => {
		const form = await superValidate(request, zod(artistSchema), { strict: true });
		if (!form.valid) {
			return fail(400, {
				form
			});
		}
		try {
			const updatedData = {
				...form.data,
				id: form.data.id?.toString()
			};

			await api().writeArtist(updatedData); // Use the API to write data
		} catch (error) {
			console.error('Error writing artist data:', error);
			return fail(500, {
				form,
				message: 'Error writing artist data'
			});
		}
		return message(form, 'success');
	}
};

import type { PageServerLoad, Actions } from '../$types.js';
import { message, superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { artistSchema } from './schema';
import { db } from '$lib/db';
import { artist } from '$lib/db/schema';
import { eq } from 'drizzle-orm';
import { clerkClient } from '@clerk/clerk-sdk-node';
import { redirect, fail } from '@sveltejs/kit';

import { redirect } from '@sveltejs/kit';
import { clerkClient } from '@clerk/clerk-sdk-node';
import { db } from '$lib/db';
import { zod } from 'zod'; // Assume import based on context
import { superValidate } from './superValidate'; // Assuming these functions are defined elsewhere
import { artistSchema } from '$lib/schemas'; // Assuming the schema definition is available

export const load: PageServerLoad = async ({ locals }) => {
	const orgId = locals.session.claims.org_id;
	if (!orgId) {
		throw redirect(500, '/error'); // Redirect to an error page
	}
	const organization = await clerkClient.organizations.getOrganization({ organizationId: orgId });
	const { name: stageName, slug } = organization;
	if (!stageName || !slug) {
		throw redirect(500, '/error');
	}
	const artistData = await db.select().from('artist').where('orgId', orgId);
	let form = await superValidate(zod(artistSchema));
	if (artistData.length > 0) {
		form = await superValidate(artistData[0], zod(artistSchema), { strict: true });
	}
	form.data = { orgId, stageName, slug, ...form.data };
	return { form };
};

export const actions: Actions = {
	default: async (request) => {
		const form = await superValidate(request, zod(artistSchema), { strict: true });
		if (!form.valid) {
			return fail(400, {
				form
			});
		}
		try {
			await db.insert(artist).values(form.data).onConflictDoUpdate({
				target: artist.orgId,
				set: form.data
			});
		} catch {
			return fail(500, {
				form
			});
		}
		return message(form, 'success');
	}
};

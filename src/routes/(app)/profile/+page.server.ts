import type { PageServerLoad, Actions } from '../$types.js';
import { message, superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { artistSchema } from './schema';
import { db } from '$lib/db';
import { artist } from '$lib/db/schema';
import { eq } from 'drizzle-orm';
import { clerkClient } from '@clerk/clerk-sdk-node';
import { redirect, fail } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ locals }) => {
	const orgId = locals.session.claims.org_id ?? null;
	if (!orgId) {
		throw redirect(500, '/error');
	}
	const organization = await clerkClient.organizations.getOrganization({ organizationId: orgId });
	const { name: stageName, slug } = organization;
	if (!stageName || !slug) {
		throw redirect(500, '/error');
	}
	const artistData = await db.select().from('artist').where(eq(artist.orgId, orgId));
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
			return fail(400, { form });
		}

		try {
			const updateExpression = {
				...form.data,
				updatedAt: new Date()
			};

			await db.insert(artist).values(form.data).onConflict(artist.orgId).doUpdate(updateExpression);

			return message(form, 'success');
		} catch (error) {
			console.error('Database operation failed', error);
			return fail(500, { form, error: 'Database operation failed' });
		}
	}
};

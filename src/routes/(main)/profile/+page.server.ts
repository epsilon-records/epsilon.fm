import type { PageServerLoad, Actions } from './$types.js';
import { message, superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { artistSchema } from './schema';
import { db } from '$lib/db';
import { artist } from '$lib/db/schema';
import { eq } from 'drizzle-orm';
import { clerkClient } from '@clerk/clerk-sdk-node';
import { redirect, fail } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ locals }) => {
	// Use type assertion to access 'session'
	const session = (locals as { session?: { claims?: { org_id?: string } } }).session;
	let form = await superValidate(zod(artistSchema));
	if (session && session.claims && session.claims.org_id) {
		const organizationId = session.claims.org_id ?? null;
		const response = await clerkClient.organizations.getOrganization({ organizationId });
		const stageName = response.name ?? null;
		const slug = response.slug ?? null;
		if (!organizationId || !stageName || !slug) {
			throw redirect(500, '/');
		}
		const data = await db.select().from(artist).where(eq(artist.orgId, organizationId));
		if (data.length != 0) {
			// Convert null values to undefined
			const formattedData = Object.fromEntries(
				Object.entries(data[0]).map(([key, value]) => [key, value === null ? undefined : value])
			);
			form = await superValidate(formattedData, zod(artistSchema), { strict: true });
		}
		form.data.orgId = organizationId;
		form.data.stageName = stageName;
		form.data.slug = slug;
	}
	return {
		form: form
	};
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
			const updatedData = { ...form.data, id: form.data.id?.toString() };
			await db.insert(artist).values(updatedData).onConflictDoUpdate({
				target: artist.orgId,
				set: updatedData
			});
		} catch {
			return fail(500, {
				form
			});
		}
		return message(form, 'success');
	}
};

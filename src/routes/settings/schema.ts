import { z } from 'zod';

export const themes = ['light', 'dark'] as const;
export const languages = ['en', 'es', 'fr'] as const;
export const allergies = ['peanuts', 'dairy', 'gluten', 'soy', 'shellfish'] as const;

export const schema = z.object({
	email: z.string().email('Please enter a valid email.'),
	bio: z.string().optional(),
	theme: z.enum(themes).default('light'),
	language: z.enum(languages).default('en'),
	marketingEmails: z.boolean().default(true),
	allergies: z.array(z.enum(allergies))
});

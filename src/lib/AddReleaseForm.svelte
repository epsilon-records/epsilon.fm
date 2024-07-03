<script lang="ts">
	import { Field, Control, Label, FieldErrors, Description } from "formsnap";
	import type { PageData } from "./$types";
	import { signupFormSchema } from "./schema.ts";
	import { zodClient } from "sveltekit-superforms/adapters";
	import { superForm } from "sveltekit-superforms";
	export let data: PageData;
 
	const form = superForm(data.form, {
		validators: zodClient(signupFormSchema),
	});
	const { form: formData, enhance } = form;
</script>
 
<form method="POST" use:enhance>
	<Field {form} name="name">
		<Control let:attrs>
			<Label>Name</Label>
			<input {...attrs} bind:value={$formData.name} />
		</Control>
		<Description>Be sure to use your real name.</Description>
		<FieldErrors />
	</Field>
	<Field {form} name="email">
		<Control let:attrs>
			<Label>Email</Label>
			<input {...attrs} type="email" bind:value={$formData.email} />
		</Control>
		<Description>It's preferred that you use your company email.</Description>
		<FieldErrors />
	</Field>
	<Field {form} name="password">
		<Control let:attrs>
			<Label>Password</Label>
			<input {...attrs} type="password" bind:value={$formData.password} />
		</Control>
		<Description>Ensure the password is at least 10 characters.</Description>
		<FieldErrors />
	</Field>
</form>
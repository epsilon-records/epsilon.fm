<script lang="ts">
	import { Field, Control, Label, Description, FieldErrors, Fieldset, Legend } from 'formsnap';
	import * as Form from '$lib/components/ui/form';
	import { Input } from '$lib/components/ui/input';
	import { artistSchema, type ArtistSchema } from './schema';
	import SuperDebug, { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import { Popover } from '$lib/components/ui/popover';

	export let data: SuperValidated<Infer<ArtistSchema>>;

	const form = superForm(data, {
		validators: zodClient(artistSchema)
	});

	const { form: formData, enhance } = form;
</script>

<form method="POST" use:enhance>
	<Form.Field {form} name="firstName">
		<Form.Control let:attrs>
			<Form.Label>First Name</Form.Label>
			<Input {...attrs} bind:value={$formData.firstName} />
		</Form.Control>
		<Form.Description>Your legal first name.</Form.Description>
		<Form.FieldErrors />
	</Form.Field>
	<Form.Field {form} name="lastName">
		<Form.Control let:attrs>
			<Form.Label>Last Name</Form.Label>
			<Input {...attrs} bind:value={$formData.lastName} />
		</Form.Control>
		<Form.Description>Your legal last name.</Form.Description>
		<Form.FieldErrors />
	</Form.Field>
	<Form.Field {form} name="email">
		<Form.Control let:attrs>
			<Form.Label>Email</Form.Label>
			<Input {...attrs} bind:value={$formData.email} />
		</Form.Control>
		<Form.Description>Your email.</Form.Description>
		<Form.FieldErrors />
	</Form.Field>
	<Form.Field {form} name="stageName">
		<Form.Control let:attrs>
			<Form.Label>Artist Stage Name</Form.Label>
			<Input {...attrs} bind:value={$formData.stageName} />
		</Form.Control>
		<Form.Description>Correct capitalization and spelling required.</Form.Description>
		<Form.FieldErrors />
	</Form.Field>
	<Form.Field {form} name="birthdate" class="flex flex-col">
		<Form.Control let:attrs>
			<Form.Label>Date of birth</Form.Label>
			<Input type="date" {...attrs} bind:value={$formData.birthdate} />
			<Form.Description>Your date of birth is used to calculator your age</Form.Description>
			<Form.FieldErrors />
			<input hidden value={$formData.birthdate} name={attrs.name} />
		</Form.Control>
	</Form.Field>
	<Form.Button>Submit</Form.Button>
	<SuperDebug data={$formData} />
</form>

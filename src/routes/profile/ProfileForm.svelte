<script lang="ts">
	import { Field, Control, Label, Description, FieldErrors, Fieldset, Legend } from 'formsnap';
	import * as Form from '$lib/components/ui/form';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
	import { artistSchema, type ArtistSchema } from './schema';
	import SuperDebug, { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';

	export let data: SuperValidated<Infer<ArtistSchema>>;

	const form = superForm(data, {
		validators: zodClient(artistSchema)
	});

	const { form: formData, enhance } = form;

	const options = {
		fields: ['address_components', 'geometry'],
		types: ['(cities)']
	};
	const placeholder = 'Destination city';
</script>

<form method="POST" use:enhance>
	<div class="mb-4 grid gap-4 sm:grid-cols-2">
		<div>
			<Form.Field {form} name="firstName">
				<Form.Control let:attrs>
					<Form.Label>First Name</Form.Label>
					<Input {...attrs} bind:value={$formData.firstName} placeholder="First Name" />
				</Form.Control>
				<Form.Description>Your legal first name.</Form.Description>
				<Form.FieldErrors />
			</Form.Field>
		</div>
		<div>
			<Form.Field {form} name="lastName">
				<Form.Control let:attrs>
					<Form.Label>Last Name</Form.Label>
					<Input {...attrs} bind:value={$formData.lastName} placeholder="Last Name" />
				</Form.Control>
				<Form.Description>Your legal last name.</Form.Description>
				<Form.FieldErrors />
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-2">
		<div>
			<Form.Field {form} name="email">
				<Form.Control let:attrs>
					<Form.Label>Email</Form.Label>
					<Input {...attrs} bind:value={$formData.email} placeholder="Email" />
				</Form.Control>
				<Form.Description>Your email address.</Form.Description>
				<Form.FieldErrors />
			</Form.Field>
		</div>
		<div>
			<Form.Field {form} name="phone" class="flex flex-col">
				<Form.Control let:attrs>
					<Form.Label>Phone</Form.Label>
					<Input {...attrs} bind:value={$formData.phone} placeholder="Phone" />
					<Form.FieldErrors />
				</Form.Control>
				<Form.Description>Your phone number.</Form.Description>
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-2">
		<div>
			<Form.Field {form} name="address" class="flex flex-col">
				<Form.Control let:attrs>
					<Form.Label>Address</Form.Label>
					<Input {...attrs} bind:value={$formData.address} placeholder="Address" />
					<Form.FieldErrors />
				</Form.Control>
				<Form.Description>Your address.</Form.Description>
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-2">
		<div>
			<Form.Field {form} name="stageName">
				<Form.Control let:attrs>
					<Form.Label>Artist Stage Name</Form.Label>
					<Input {...attrs} bind:value={$formData.stageName} placeholder="Stage Name" />
				</Form.Control>
				<Form.Description>Correct capitalisation and spelling required.</Form.Description>
				<Form.FieldErrors />
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-2">
		<div>
			<Form.Field {form} name="biography">
				<Form.Control let:attrs>
					<Form.Label>Artist Stage Name</Form.Label>
					<Textarea {...attrs} bind:value={$formData.biography} placeholder="Biography" />
				</Form.Control>
				<Form.Description>Your artist biography.</Form.Description>
				<Form.FieldErrors />
			</Form.Field>
		</div>
	</div>
	<div>
		<Form.Button>Submit</Form.Button>
		<SuperDebug data={$formData} />
	</div>
</form>

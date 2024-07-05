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

<!-- use:enhance -->
<form method="POST" action="?/save">
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
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
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="biography">
				<Form.Control let:attrs>
					<Form.Label>Artist Biography</Form.Label>
					<Textarea {...attrs} bind:value={$formData.biography} placeholder="Biography" />
				</Form.Control>
				<Form.Description>Your artist biography.</Form.Description>
				<Form.FieldErrors />
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="stageName">
				<Form.Control let:attrs>
					<Form.Label>Spotify Artist Link</Form.Label>
					<Input
						{...attrs}
						bind:value={$formData.spotifyArtistLink}
						placeholder="Spotify Artist Link"
					/>
				</Form.Control>
				<Form.Description>Your Spotify artist profile link.</Form.Description>
				<Form.FieldErrors />
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="youtubeChannelLink">
				<Form.Control let:attrs>
					<Form.Label>YouTube Channel Link</Form.Label>
					<Input
						{...attrs}
						bind:value={$formData.youtubeChannelLink}
						placeholder="YouTube Channel Link"
					/>
				</Form.Control>
				<Form.Description>Your YouTube artist channel link.</Form.Description>
				<Form.FieldErrors />
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="instagramProfileLink">
				<Form.Control let:attrs>
					<Form.Label>Instagram Profile Link</Form.Label>
					<Input
						{...attrs}
						bind:value={$formData.instagramProfileLink}
						placeholder="Instagram Profile Link"
					/>
				</Form.Control>
				<Form.Description>Your YouTube artist channel link.</Form.Description>
				<Form.FieldErrors />
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="facebookProfileLink">
				<Form.Control let:attrs>
					<Form.Label>Facebook Profile Link</Form.Label>
					<Input
						{...attrs}
						bind:value={$formData.facebookProfileLink}
						placeholder="Facebook Profile Link"
					/>
				</Form.Control>
				<Form.Description>Your Facebook artist profile link.</Form.Description>
				<Form.FieldErrors />
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="xProfileLink">
				<Form.Control let:attrs>
					<Form.Label>X Profile Link</Form.Label>
					<Input {...attrs} bind:value={$formData.xProfileLink} placeholder="X Profile Link" />
				</Form.Control>
				<Form.Description>Your X artist profile link.</Form.Description>
				<Form.FieldErrors />
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="tiktokProfileLink">
				<Form.Control let:attrs>
					<Form.Label>TikTok Profile Link</Form.Label>
					<Input
						{...attrs}
						bind:value={$formData.tiktokProfileLink}
						placeholder="TikTok Profile Link"
					/>
				</Form.Control>
				<Form.Description>Your TikTok artist profile link.</Form.Description>
				<Form.FieldErrors />
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="soundcloudProfileLink">
				<Form.Control let:attrs>
					<Form.Label>SoundCloud Profile Link</Form.Label>
					<Input
						{...attrs}
						bind:value={$formData.soundcloudProfileLink}
						placeholder="SoundCloud Profile Link"
					/>
				</Form.Control>
				<Form.Description>Your SoundCloud artist profile link.</Form.Description>
				<Form.FieldErrors />
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="songkickProfileLink">
				<Form.Control let:attrs>
					<Form.Label>Songkick Profile Link</Form.Label>
					<Input
						{...attrs}
						bind:value={$formData.songkickProfileLink}
						placeholder="Songkick Profile Link"
					/>
				</Form.Control>
				<Form.Description>Your Songkick artist profile link.</Form.Description>
				<Form.FieldErrors />
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="bandsintownProfileLink">
				<Form.Control let:attrs>
					<Form.Label>Bandsintown Profile Link</Form.Label>
					<Input
						{...attrs}
						bind:value={$formData.bandsintownProfileLink}
						placeholder="Bandsintown Profile Link"
					/>
				</Form.Control>
				<Form.Description>Your Bandsintown artist profile link.</Form.Description>
				<Form.FieldErrors />
			</Form.Field>
		</div>
	</div>
	<div>
		<Form.Button>Submit</Form.Button>
	</div>
	<div class="m-4">
		<SuperDebug data={$formData} />
	</div>
</form>

<script lang="ts">
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
	import * as Form from '$lib/components/ui/form';
	import { artistSchema, type ArtistSchema } from '$lib/schema';
	import SuperDebug from 'sveltekit-superforms';
	import { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import toast from 'svelte-french-toast';
	import success from '$lib/audio/success.mp3';
	import { tick } from 'svelte';
	import { confetti } from '@neoconfetti/svelte';
	export let data: SuperValidated<Infer<ArtistSchema>>;
	export let dataType: 'form' | 'json' = 'form';

	let isVisible = false;
	const form = superForm(data, {
		dataType: dataType,
		validators: zodClient(artistSchema),
		resetForm: false,
		async onUpdated({ form }) {
			if (form.message == 'success') {
				const audio = new Audio();
				audio.src = success;
				audio.load();
				isVisible = false;
				await tick();
				isVisible = true;
				audio.play();
				toast.success('Successfully saved!');
			}
		}
	});
	const { form: formData, enhance } = form;
</script>

<form method="POST" use:enhance>
	<Form.Field {form} name="stage_name">
		<Form.Control let:attrs>
			<Form.Label>Artist Stage Name</Form.Label>
			<Input {...attrs} class="bg-muted text-xl" bind:value={$formData.stage_name} readonly />
		</Form.Control>
		<Form.Description>
			Your artist stage name may be updated by changing your organization name, noting that correct
			spelling and capitalization are required to ensure proper music delivery.
		</Form.Description>
	</Form.Field>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="org_id">
				<Form.Control let:attrs>
					<Form.Label>ID</Form.Label>
					<Input {...attrs} class="bg-muted" bind:value={$formData.org_id} readonly />
				</Form.Control>
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="slug">
				<Form.Control let:attrs>
					<Form.Label>Artist Website</Form.Label>
					<Input {...attrs} class="bg-muted" bind:value={$formData.slug} readonly />
				</Form.Control>
				<div class="grid gap-4 text-xs">
					<Form.Description>
						Your artist website may me accessed at <a
							class="text-blue-500"
							href="https://{$formData.slug}.epsilon.fm">{$formData.slug}.epsilon.fm</a
						> and may be updated by changing your organization slug.
					</Form.Description>
				</div>
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="email">
				<Form.Control let:attrs>
					<Form.Label>Artist Contact Email</Form.Label>
					<Input {...attrs} bind:value={$formData.email} placeholder="Artist Contact Email" />
				</Form.Control>
				<div class="grid gap-4 text-xs sm:grid-cols-2">
					<Form.Description class="">Your artist contact email.</Form.Description>
					<Form.FieldErrors class="text-right text-red-500" />
				</div>
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
				<div class="grid gap-4 text-xs sm:grid-cols-2">
					<Form.Description class="">Your artist biography.</Form.Description>
					<Form.FieldErrors class="text-right text-red-500" />
				</div>
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="spotify_artist_link">
				<Form.Control let:attrs>
					<Form.Label>Spotify Artist Link</Form.Label>
					<Input
						{...attrs}
						bind:value={$formData.spotify_artist_link}
						placeholder="Spotify Artist Link"
					/>
				</Form.Control>
				<div class="grid gap-4 text-xs sm:grid-cols-2">
					<Form.Description class="">Your Spotify artist profile link.</Form.Description>
					<Form.FieldErrors class="text-right text-red-500" />
				</div>
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="youtube_channel_link">
				<Form.Control let:attrs>
					<Form.Label>YouTube Channel Link</Form.Label>
					<Input
						{...attrs}
						bind:value={$formData.youtube_channel_link}
						placeholder="YouTube Channel Link"
					/>
				</Form.Control>
				<div class="grid gap-4 text-xs sm:grid-cols-2">
					<Form.Description class="">Your YouTube artist channel link.</Form.Description>
					<Form.FieldErrors class="text-right text-red-500" />
				</div>
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="instagram_profile_link">
				<Form.Control let:attrs>
					<Form.Label>Instagram Profile Link</Form.Label>
					<Input
						{...attrs}
						bind:value={$formData.instagram_profile_link}
						placeholder="Instagram Profile Link"
					/>
				</Form.Control>
				<div class="grid gap-4 text-xs sm:grid-cols-2">
					<Form.Description class="">Your Instagram artist profile link.</Form.Description>
					<Form.FieldErrors class="text-right text-red-500" />
				</div>
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="facebook_profile_link">
				<Form.Control let:attrs>
					<Form.Label>Facebook Profile Link</Form.Label>
					<Input
						{...attrs}
						bind:value={$formData.facebook_profile_link}
						placeholder="Facebook Profile Link"
					/>
				</Form.Control>
				<div class="grid gap-4 text-xs sm:grid-cols-2">
					<Form.Description class="">Your Facebook artist profile link.</Form.Description>
					<Form.FieldErrors class="text-right text-red-500" />
				</div>
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="x_profile_link">
				<Form.Control let:attrs>
					<Form.Label>X Profile Link</Form.Label>
					<Input {...attrs} bind:value={$formData.x_profile_link} placeholder="X Profile Link" />
				</Form.Control>
				<div class="grid gap-4 text-xs sm:grid-cols-2">
					<Form.Description class="">Your X artist profile link.</Form.Description>
					<Form.FieldErrors class="text-right text-red-500" />
				</div>
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="tiktok_profile_link">
				<Form.Control let:attrs>
					<Form.Label>TikTok Profile Link</Form.Label>
					<Input
						{...attrs}
						bind:value={$formData.tiktok_profile_link}
						placeholder="TikTok Profile Link"
					/>
				</Form.Control>
				<div class="grid gap-4 text-xs sm:grid-cols-2">
					<Form.Description class="">Your TikTok artist profile link.</Form.Description>
					<Form.FieldErrors class="text-right text-red-500" />
				</div>
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="soundcloud_profile_link">
				<Form.Control let:attrs>
					<Form.Label>SoundCloud Profile Link</Form.Label>
					<Input
						{...attrs}
						bind:value={$formData.soundcloud_profile_link}
						placeholder="SoundCloud Profile Link"
					/>
				</Form.Control>
				<div class="grid gap-4 text-xs sm:grid-cols-2">
					<Form.Description class="">Your SoundCloud artist profile link.</Form.Description>
					<Form.FieldErrors class="text-right text-red-500" />
				</div>
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="songkick_profile_link">
				<Form.Control let:attrs>
					<Form.Label>Songkick Profile Link</Form.Label>
					<Input
						{...attrs}
						bind:value={$formData.songkick_profile_link}
						placeholder="Songkick Profile Link"
					/>
				</Form.Control>
				<div class="grid gap-4 text-xs sm:grid-cols-2">
					<Form.Description class="">Your Songkick artist profile link.</Form.Description>
					<Form.FieldErrors class="text-right text-red-500" />
				</div>
			</Form.Field>
		</div>
	</div>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Form.Field {form} name="bandsintown_profile_link">
				<Form.Control let:attrs>
					<Form.Label>Bandsintown Profile Link</Form.Label>
					<Input
						{...attrs}
						bind:value={$formData.bandsintown_profile_link}
						placeholder="Bandsintown Profile Link"
					/>
				</Form.Control>
				<div class="grid gap-4 text-xs sm:grid-cols-2">
					<Form.Description class="">Your Bandsintown artist profile link.</Form.Description>
					<Form.FieldErrors class="text-right text-red-500" />
				</div>
			</Form.Field>
		</div>
	</div>
	<div>
		<Form.Button>Submit</Form.Button>
	</div>
	{#if isVisible}
		<div use:confetti></div>
	{/if}
	{#if import.meta.env.MODE == 'development'}
		<div class="m-4">
			<SuperDebug data={$formData} />
		</div>
	{/if}
</form>

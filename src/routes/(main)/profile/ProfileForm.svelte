<script lang="ts">
	import { Field, Control, Label, FieldErrors, Description } from 'formsnap';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
	import * as Form from '$lib/components/ui/form';
	import { artistSchema, type ArtistSchema } from './schema';
	// import SuperDebug from 'sveltekit-superforms';
	import { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
	import toast from 'svelte-french-toast';
	import success from '$lib/audio/success.mp3';
	import { tick } from 'svelte';
	import { confetti } from '@neoconfetti/svelte';
	export let data: SuperValidated<Infer<ArtistSchema>>;

	let isVisible = false;
	const form = superForm(data, {
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

<SignedIn>
	<form method="POST" use:enhance>
		<div class="mb-4 grid gap-4 sm:grid-cols-1">
			<div>
				<Field {form} name="stageName">
					<Control let:attrs>
						<Label>Artist Stage Name</Label>
						<Input {...attrs} class="bg-muted text-xl" bind:value={$formData.stageName} readonly />
					</Control>
					<div class="grid gap-4 text-xs">
						<Description>
							Your artist stage name may be updated by changing your organization name, noting that
							correct spelling and capitalization are required to ensure proper music delivery.
						</Description>
					</div>
				</Field>
			</div>
		</div>
		<div class="mb-4 grid gap-4 sm:grid-cols-1">
			<div>
				<Field {form} name="orgId">
					<Control let:attrs>
						<Label>ID</Label>
						<Input {...attrs} class="bg-muted" bind:value={$formData.orgId} readonly />
					</Control>
				</Field>
			</div>
		</div>
		<div class="mb-4 grid gap-4 sm:grid-cols-1">
			<div>
				<Field {form} name="slug">
					<Control let:attrs>
						<Label>Artist Website</Label>
						<Input {...attrs} class="bg-muted" bind:value={$formData.slug} readonly />
					</Control>
					<div class="grid gap-4 text-xs">
						<Description>
							Your artist website may me accessed at <a
								class="text-blue-500"
								href="https://{$formData.slug}.epsilon.fm">{$formData.slug}.epsilon.fm</a
							> and may be updated by changing your organization slug.
						</Description>
					</div>
				</Field>
			</div>
		</div>
		<div class="mb-4 grid gap-4 sm:grid-cols-1">
			<div>
				<Field {form} name="email">
					<Control let:attrs>
						<Label>Artist Contact Email</Label>
						<Input {...attrs} bind:value={$formData.email} placeholder="Artist Contact Email" />
					</Control>
					<div class="grid gap-4 text-xs sm:grid-cols-2">
						<Description class="">Your artist contact email.</Description>
						<FieldErrors class="text-right text-red-500" />
					</div>
				</Field>
			</div>
		</div>
		<div class="mb-4 grid gap-4 sm:grid-cols-1">
			<div>
				<Field {form} name="biography">
					<Control let:attrs>
						<Label>Artist Biography</Label>
						<Textarea {...attrs} bind:value={$formData.biography} placeholder="Biography" />
					</Control>
					<div class="grid gap-4 text-xs sm:grid-cols-2">
						<Description class="">Your artist biography.</Description>
						<FieldErrors class="text-right text-red-500" />
					</div>
				</Field>
			</div>
		</div>
		<div class="mb-4 grid gap-4 sm:grid-cols-1">
			<div>
				<Field {form} name="spotifyArtistLink">
					<Control let:attrs>
						<Label>Spotify Artist Link</Label>
						<Input
							{...attrs}
							bind:value={$formData.spotifyArtistLink}
							placeholder="Spotify Artist Link"
						/>
					</Control>
					<div class="grid gap-4 text-xs sm:grid-cols-2">
						<Description class="">Your Spotify artist profile link.</Description>
						<FieldErrors class="text-right text-red-500" />
					</div>
				</Field>
			</div>
		</div>
		<div class="mb-4 grid gap-4 sm:grid-cols-1">
			<div>
				<Field {form} name="youtubeChannelLink">
					<Control let:attrs>
						<Label>YouTube Channel Link</Label>
						<Input
							{...attrs}
							bind:value={$formData.youtubeChannelLink}
							placeholder="YouTube Channel Link"
						/>
					</Control>
					<div class="grid gap-4 text-xs sm:grid-cols-2">
						<Description class="">Your YouTube artist channel link.</Description>
						<FieldErrors class="text-right text-red-500" />
					</div>
				</Field>
			</div>
		</div>
		<div class="mb-4 grid gap-4 sm:grid-cols-1">
			<div>
				<Field {form} name="instagramProfileLink">
					<Control let:attrs>
						<Label>Instagram Profile Link</Label>
						<Input
							{...attrs}
							bind:value={$formData.instagramProfileLink}
							placeholder="Instagram Profile Link"
						/>
					</Control>
					<div class="grid gap-4 text-xs sm:grid-cols-2">
						<Description class="">Your Instagram artist profile link.</Description>
						<FieldErrors class="text-right text-red-500" />
					</div>
				</Field>
			</div>
		</div>
		<div class="mb-4 grid gap-4 sm:grid-cols-1">
			<div>
				<Field {form} name="facebookProfileLink">
					<Control let:attrs>
						<Label>Facebook Profile Link</Label>
						<Input
							{...attrs}
							bind:value={$formData.facebookProfileLink}
							placeholder="Facebook Profile Link"
						/>
					</Control>
					<div class="grid gap-4 text-xs sm:grid-cols-2">
						<Description class="">Your Facebook artist profile link.</Description>
						<FieldErrors class="text-right text-red-500" />
					</div>
				</Field>
			</div>
		</div>
		<div class="mb-4 grid gap-4 sm:grid-cols-1">
			<div>
				<Field {form} name="xProfileLink">
					<Control let:attrs>
						<Label>X Profile Link</Label>
						<Input {...attrs} bind:value={$formData.xProfileLink} placeholder="X Profile Link" />
					</Control>
					<div class="grid gap-4 text-xs sm:grid-cols-2">
						<Description class="">Your X artist profile link.</Description>
						<FieldErrors class="text-right text-red-500" />
					</div>
				</Field>
			</div>
		</div>
		<div class="mb-4 grid gap-4 sm:grid-cols-1">
			<div>
				<Field {form} name="tiktokProfileLink">
					<Control let:attrs>
						<Label>TikTok Profile Link</Label>
						<Input
							{...attrs}
							bind:value={$formData.tiktokProfileLink}
							placeholder="TikTok Profile Link"
						/>
					</Control>
					<div class="grid gap-4 text-xs sm:grid-cols-2">
						<Description class="">Your TikTok artist profile link.</Description>
						<FieldErrors class="text-right text-red-500" />
					</div>
				</Field>
			</div>
		</div>
		<div class="mb-4 grid gap-4 sm:grid-cols-1">
			<div>
				<Field {form} name="soundcloudProfileLink">
					<Control let:attrs>
						<Label>SoundCloud Profile Link</Label>
						<Input
							{...attrs}
							bind:value={$formData.soundcloudProfileLink}
							placeholder="SoundCloud Profile Link"
						/>
					</Control>
					<div class="grid gap-4 text-xs sm:grid-cols-2">
						<Description class="">Your SoundCloud artist profile link.</Description>
						<FieldErrors class="text-right text-red-500" />
					</div>
				</Field>
			</div>
		</div>
		<div class="mb-4 grid gap-4 sm:grid-cols-1">
			<div>
				<Field {form} name="songkickProfileLink">
					<Control let:attrs>
						<Label>Songkick Profile Link</Label>
						<Input
							{...attrs}
							bind:value={$formData.songkickProfileLink}
							placeholder="Songkick Profile Link"
						/>
					</Control>
					<div class="grid gap-4 text-xs sm:grid-cols-2">
						<Description class="">Your Songkick artist profile link.</Description>
						<FieldErrors class="text-right text-red-500" />
					</div>
				</Field>
			</div>
		</div>
		<div class="mb-4 grid gap-4 sm:grid-cols-1">
			<div>
				<Field {form} name="bandsintownProfileLink">
					<Control let:attrs>
						<Label>Bandsintown Profile Link</Label>
						<Input
							{...attrs}
							bind:value={$formData.bandsintownProfileLink}
							placeholder="Bandsintown Profile Link"
						/>
					</Control>
					<div class="grid gap-4 text-xs sm:grid-cols-2">
						<Description class="">Your Bandsintown artist profile link.</Description>
						<FieldErrors class="text-right text-red-500" />
					</div>
				</Field>
			</div>
		</div>
		<div>
			<Form.Button>Submit</Form.Button>
		</div>
		{#if isVisible}
			<div use:confetti />
		{/if}
		<!-- <div class="m-4">
			<SuperDebug data={$formData} />
		</div> -->
	</form>
</SignedIn>

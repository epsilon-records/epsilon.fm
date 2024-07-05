<script lang="ts">
	import { Field, Control, Label, FieldErrors, Description } from 'formsnap';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
	import { Button } from '$lib/components/ui/button';
	import { artistSchema, type ArtistSchema } from './schema';
	import SuperDebug, { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';

	export let data: SuperValidated<Infer<ArtistSchema>>;

	// formsnap.dev/docs
	const form = superForm(data, {
		validators: zodClient(artistSchema)
	});
	const { form: formData, enhance } = form;
</script>

<form method="POST" use:enhance>
	<Field {form} name="orgId">
		<Control let:attrs>
			<Input {...attrs} bind:value={$formData.orgId} type="hidden" />
		</Control>
		<FieldErrors />
	</Field>
	<div class="mb-4 grid gap-4 sm:grid-cols-1">
		<div>
			<Field {form} name="stageName">
				<Control let:attrs>
					<Label class="text-lg">Artist Stage Name</Label>
					<Input {...attrs} bind:value={$formData.stageName} placeholder="Stage Name" />
				</Control>
				<div class="grid gap-4 sm:grid-cols-2">
					<Description class="text-sm">Correct capitalisation and spelling required.</Description>
					<FieldErrors class="text-sm text-red-500" />
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
				<Description>Your artist biography.</Description>
				<FieldErrors />
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
				<Description>Your Spotify artist profile link.</Description>
				<FieldErrors />
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
				<Description>Your YouTube artist channel link.</Description>
				<FieldErrors />
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
				<Description>Your Instagram artist profile link.</Description>
				<FieldErrors />
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
				<Description>Your Facebook artist profile link.</Description>
				<FieldErrors />
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
				<Description>Your X artist profile link.</Description>
				<FieldErrors />
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
				<Description>Your TikTok artist profile link.</Description>
				<FieldErrors />
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
				<Description>Your SoundCloud artist profile link.</Description>
				<FieldErrors />
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
				<Description>Your Songkick artist profile link.</Description>
				<FieldErrors />
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
				<Description>Your Bandsintown artist profile link.</Description>
				<FieldErrors />
			</Field>
		</div>
	</div>
	<div>
		<Button>Submit</Button>
	</div>
	<div class="m-4">
		<SuperDebug data={$formData} />
	</div>
</form>

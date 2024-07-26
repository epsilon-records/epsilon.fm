<script>
	import { Meta, Story, Template } from '@storybook/addon-svelte-csf';

	import ProfileForm from './ProfileForm.svelte';
</script>

<Meta component={ProfileForm} autodocs />

<Template let:args>
	<ProfileForm {...args} />
</Template>

<Story
	name="Default"
	args={{
		dataType: 'json',
		data: {
			form: {
				status: 200,
				id: '8763fae1-37be-48ff-8a96-669dd3f1e5e4',
				created_at: '2024-07-21T08:54:30.396918+00:00',
				updated_at: '2024-07-21T08:54:30.396923+00:00',
				org_id: 'org_2j0FF4BnRtAmzzzRi8tWFaM37W4',
				slug: 'vozz-rich',
				stage_name: 'Vozz Rich',
				media_url: undefined,
				email: 'vozzrich@gmail.com',
				biography: 'Test',
				spotify_artist_link: '',
				youtube_channel_link: '',
				instagram_profile_link: '',
				facebook_profile_link: '',
				x_profile_link: '',
				tiktok_profile_link: '',
				soundcloud_profile_link: '',
				songkick_profile_link: '',
				bandsintown_profile_link: ''
			}
		}
	}}
/>

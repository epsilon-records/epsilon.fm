import axios from 'axios';

export interface MusicfetchImage {
	url: string;
	width: number;
	height: number;
}

export interface MusicfetchArtist {
	type: 'artist';
	name: string;
	description: string;
	image: MusicfetchImage;
	artists: MusicfetchArtist[];
	albums: MusicfetchAlbum[];
	videos: MusicfetchVideo[];
	services: {
		[serviceType: string]: {
			id: string;
			link: string;
		};
	};
}

export interface MusicfetchAlbum {
	type: 'album';
	name: string;
	upc?: string;
	totalTracks: number;
	releaseDate: string;
	previewUrl?: string;
	image: MusicfetchImage;
	artists: MusicfetchArtist[];
	tracks?: MusicfetchTrack[];
	label: string;
	copyright: string;
	services: {
		[serviceType: string]: {
			id: string;
			link: string;
		};
	};
}

export interface MusicfetchTrack {
	type: 'track';
	name: string;
	isrc?: string;
	duration: number;
	label: string;
	copyright: string;
	isExplicit: boolean;
	previewUrl?: string;
	image: MusicfetchImage;
	artists: MusicfetchArtist[];
	albums: MusicfetchAlbum[];
	services: {
		[serviceType: string]: {
			id: string;
			link: string;
		};
	};
}

export interface MusicfetchVideo {
	// Add properties for MusicfetchVideo if available
}

export interface MusicfetchResponse {
	result: MusicfetchTrack | MusicfetchAlbum | MusicfetchArtist;
	performance?: unknown; // Add specific type if available
}

export class Musicfetch {
	private token: string;

	constructor(token: string) {
		this.token = token;
	}

	public async lookupArtist(
		url: string,
		services: string[],
		country?: string
	): Promise<MusicfetchArtist> {
		const endpoint = 'https://api.musicfetch.io/url';
		const params: { [key: string]: string } = {
			url: url,
			services: services.join(',')
		};

		if (country) {
			params['country'] = country;
		}
		const response = await axios.get<MusicfetchResponse>(endpoint, {
			params: params,
			headers: {
				'x-musicfetch-token': this.token
			}
		});
		return response.data.result as MusicfetchArtist;
	}
}

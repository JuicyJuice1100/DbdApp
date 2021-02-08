import { Component, OnInit } from '@angular/core';
import * as myBuilds from 'src/assets/data/builds.json'

@Component({
	selector: 'app-my-builds',
	templateUrl: './my-builds.page.html',
	styleUrls: ['./my-builds.page.scss'],
})
export class MyBuildsPage implements OnInit {

	constructor() { }

	myBuilds: any = (myBuilds as any).default;
	myBuildsBackup: any = this.myBuilds;

	async filterList(event) {
		this.myBuilds = this.myBuildsBackup
		const searchTerm = event.srcElement.value;

		if(!searchTerm){
			return;
		}

		this.myBuilds = this.myBuilds.filter(q => q.name.includes(searchTerm))
	}

	ngOnInit() {
		
	}

}

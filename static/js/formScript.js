//add Education
document.querySelector(".educationBox").addEventListener("click", (e) => {
  if (e.target.name == "addEdu") {
    addEducation();
  }
  if (e.target.name == "removeEdu") {
    const edudiv = e.target.closest(".eduinfo");
    edudiv.remove();
  }
});
function addEducation() {
  let education = document.querySelector(".educationBox");
  let edudiv = document.createElement("div");
  edudiv.className = "eduinfo";
  edudiv.innerHTML = `<label for="degree">Degree</label><br />
<input type="text" name="degree[]" id="degree" /><br /><br />
<label for="start">Start year</label><br />
<input type="text" name="start[]" id="start" /><br /><br />
<label for="end">End Year</label><br />
<input type="text" name="end[]" id="end" /><br /><br />
<label for="uni">University name</label><br />
<input type="text" name="uni[]" id="uni" /><br /><br />
<button name="addEdu" type="button">Add Education</button>
<button name="removeEdu" type="button">remove Education</button>
`;
  education.appendChild(edudiv);
} //add Language
document.querySelector(".language").addEventListener("click", (e) => {
  if (e.target.name == "addlng") {
    addlng();
  }
  if (e.target.name == "removelng") {
    const lngdiv = e.target.closest(".language");
    lngdiv.remove();
  }
});
function addlng() {
  let language = document.querySelector(".language");
  let lngdiv = document.createElement("div");
  lngdiv.className = "language";
  lngdiv.innerHTML = `<label for="name">language</label> <input type="text" name="lanname[]" /><br />
Enter percentage of Expertise
<input type="text" name="lanper[]" /><br /><br />
<button name="addlng" type="button">Add language</button>
<button name="removelng" type="button">remove language</button>`;
  language.appendChild(lngdiv);
} //add Experience
document.querySelector(".experienceBox").addEventListener("click", (e) => {
  if (e.target.name == "addExperience") {
    addExperience();
  }
  if (e.target.name == "removeExp") {
    let expdiv = e.target.closest(".experience");
    expdiv.remove();
  }
});
function addExperience() {
  let experienceBox = document.querySelector(".experienceBox");
  let expdiv = document.createElement("div");
  expdiv.className = "experience";
  expdiv.innerHTML = `<label for="exprience">Experience</label>
Enter start Year:
<input type="text" name="ex-start" />
Enter end Year:
<input type="text" name="ex-end" />
Enter company name:
<input type="text" name="cname" />
Enter job-role:
<input type="text" name="job-role" />
Enter job description
<textarea name="job-des"></textarea><br /><br />

<button type="button" name="addExprience">Add Exprience</button><br /><br />;
<button type="button" name="removeExp">Remove Exprience</button><br /><br />`;
  experienceBox.appendChild(expdiv);
} // add skill
document.querySelector(".skillBox").addEventListener("click", (e) => {
  if (e.target.name == "addSkill") {
    addSkill();
  } else if (e.target.name == "removeSkill") {
    let skills = e.target.closest(".skills");
    skills.remove();
  }
});
function addSkill() {
  let skillBox = document.querySelector(".skillBox");
  let skills = document.createElement("div");
  skills.className = "skills";
  skills.innerHTML = ` Enter Skill name:
<input type="text" name="skill-name[]" />
Enter percentage of Expertise
<input type="text" name="skill-per[]" />
<button type="button" name="addSkill">Add Skill</button>
<button type="button" name="removeSkill">Remove Skill</button>`;
  skillBox.appendChild(skills);
} //addExpertise
document.querySelector(".expBox").addEventListener("click", (e) => {
  if (e.target.name == "addExpertise") {
    addExpertise();
  } else if (e.target.name == "removeExpertise") {
    let expert = e.target.closest(".expInfo");
    expert.remove();
  }
});
function addExpertise() {
  const expBox = document.querySelector(".expBox");
  let expInfo = document.createElement("div");
  expInfo.className = "expInfo";
  expInfo.innerHTML = `
<input type="text" name="expert[]" class="expert" id="expert" /><br /><br />

<button name="addExpertise" type="button">Add Expertise</button>
<button type="button" name="removeExpertise">Remove Skill</button>`;
  expBox.appendChild(expInfo);
}
